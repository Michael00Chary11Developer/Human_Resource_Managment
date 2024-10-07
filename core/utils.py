class CleanData(str):
    
    def created_clean(self):
        return ''.join(self.lower().split())