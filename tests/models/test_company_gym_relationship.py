from init import db

def test_company_gym_relationship(app):
    """Test that a company can have multiple gyms"""
    from models import Company, Gym
    
    with app.app_context():
        # Create a company
        company = Company(
            name="Test Company",
            website="www.testcompany.com"
        )
        db.session.add(company)
        db.session.commit()
        
        # Create gyms belonging to this company
        gym1 = Gym(
            company_id=company.id,
            city="City 1",
            street_address="123 Test St",
            name="Gym 1"
        )
        
        gym2 = Gym(
            company_id=company.id,
            city="City 2",
            street_address="456 Test St",
            name="Gym 2"
        )
        
        db.session.add_all([gym1, gym2])
        db.session.commit()
        
        # Test the forward relationship (gym → company)
        assert gym1.company.name == "Test Company"
        assert gym2.company.website == "www.testcompany.com"
        
        # Test the backward relationship (company → gyms)
        assert len(company.gym) == 2
        assert company.gym[0].name == "Gym 1"
        assert company.gym[1].name == "Gym 2"

