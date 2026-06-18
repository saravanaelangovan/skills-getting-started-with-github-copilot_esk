def test_get_activities_returns_all_activities_with_expected_schema(client):
    # Arrange
    expected_min_activity_count = 1

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) >= expected_min_activity_count

    for activity_name, details in payload.items():
        assert isinstance(activity_name, str)
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
