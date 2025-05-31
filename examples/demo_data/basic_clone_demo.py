
# with ❤️ and a commitment to ethical technology

"""
Basic demonstration of Medical Virtual Clone concept
Warning: This is a simplified demo. Production code requires extensive security measures.
"""

from cryptography.fernet import Fernet
import json
import hashlib
from datetime import datetime, timedelta


class MedicalVirtualClone:
    def __init__(self):
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.access_log = []

    def create_clone(self, medical_data):
        """Create encrypted virtual clone from medical data"""
        # Standardize data format
        standardized = self._standardize_data(medical_data)

        # Encrypt
        encrypted = self.cipher.encrypt(json.dumps(standardized).encode())

        # Generate temporary access key
        access_key = self._generate_access_key()

        return {
            'clone_id': hashlib.sha256(encrypted).hexdigest()[:16],
            'encrypted_data': encrypted,
            'access_key': access_key
        }

    def _standardize_data(self, data):
        """Remove identifying information while preserving medical relevance"""
        return {
            'biological_sex': data.get('sex'),
            'medical_history': data.get('history'),
            'vitals': data.get('vitals'),
            'medications': data.get('medications'),
            # Explicitly exclude: name, address, SSN, etc.
        }

    def _generate_access_key(self):
        """Generate self-destructing access key"""
        return {
            'key': Fernet.generate_key().decode(),
            'expires': (datetime.now() + timedelta(hours=1)).isoformat()
        }


# Demo usage
if __name__ == "__main__":
    clone_system = MedicalVirtualClone()

    # Sample medical data
    patient_data = {
        'name': 'REDACTED',  # Would be removed
        'sex': 'F',
        'history': ['hypertension', 'diabetes_type2'],
        'vitals': {'bp': '120/80', 'heart_rate': 72},
        'medications': ['metformin', 'lisinopril']
    }

    # Create virtual clone
    virtual_clone = clone_system.create_clone(patient_data)
    print(f"Virtual Clone Created: {virtual_clone['clone_id']}")
    print(f"Access Key (expires in 1 hour): {virtual_clone['access_key']['key'][:20]}...")