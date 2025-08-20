def test_company_creation(app):
    """Test we can create a company based on the company model"""
    from models import Company
    with app.app_context():
        company = Company(
            name="simplecompany",
            website="www.company.com",
            )
        assert company.name == "simplecompany"
        assert company.website == "www.company.com"