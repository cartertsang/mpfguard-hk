from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base
from cryptography.fernet import Fernet
from app.core.config import settings
import base64

# Prod: key from KMS/env, base64 encoded
ENCRYPT_KEY = settings.get('ENCRYPT_KEY', b'demo_key_32_bytes_long_enough_for_fernet==')  # MVP demo
cipher_suite = Fernet(base64.urlsafe_b64encode(ENCRYPT_KEY.ljust(32, b'0')[:32]))

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    clerk_user_id = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    mpf_employer_id = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    employees = relationship('Employee', back_populates='company')

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    name = Column(String(255), nullable=False)
    id_number_encrypted = Column(Text)  # PDPO PII encrypt
    bank_account_encrypted = Column(Text)
    company = relationship('Company', back_populates='employees')

    @property
    def id_number(self):
        return cipher_suite.decrypt(self.id_number_encrypted.encode()).decode() if self.id_number_encrypted else None

    @id_number.setter
    def id_number(self, value):
        self.id_number_encrypted = cipher_suite.encrypt(value.encode()).decode() if value else None

    @property
    def bank_account(self):
        return cipher_suite.decrypt(self.bank_account_encrypted.encode()).decode() if self.bank_account_encrypted else None

    @bank_account.setter
    def bank_account(self, value):
        self.bank_account_encrypted = cipher_suite.encrypt(value.encode()).decode() if value else None

class PayrollRecord(Base):
    __tablename__ = 'payroll_records'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    month_year = Column(String(7), index=True)  # YYYY-MM
    gross_salary = Column(Float, nullable=False)
    overtime = Column(Float, default=0.0)
    commission = Column(Float, default=0.0)
    unpaid_days = Column(Float, default=0.0)
    worked_days = Column(Float, default=22.0)
    notes = Column(Text)

class MPFSubmission(Base):
    __tablename__ = 'mpf_submissions'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    month_year = Column(String(7), index=True)
    relevant_income = Column(Float)
    ee_contrib = Column(Float)
    er_contrib = Column(Float)
    csv_path = Column(String(500))
    status = Column(String(50), default='draft')  # draft/approved/exported
    approved_by = Column(String(255))  # Clerk user
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    action = Column(String(100), nullable=False)
    entity_type = Column(String(50))  # 'payroll', 'mpf'
    entity_id = Column(Integer)
    old_value = Column(Text)
    new_value = Column(Text)
    user_id = Column(String(255))  # Clerk
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    # Immutable: DB trigger prevent DELETE/UPDATE