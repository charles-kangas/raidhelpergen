import pytest

from app import create_raid_helper_cmd, get_roles_for_users, get_role_for_user, get_role_cmd_for_role_and_users


def test_get_role_cmd_for_role_and_users_single_role_user():
    result = get_role_cmd_for_role_and_users(users=["Doom"], role="Combat")
    assert result == "Combat [Doom]"


def test_get_role_cmd_for_role_and_users_single_role_mult_users():
    result = get_role_cmd_for_role_and_users(users=["Gloom", "djhedgehog", "Phaser"], role="Fire")
    assert result == "Fire [Djhedgehog, Gloom, Phaser]"


def test_create_raid_helper_cmd_multiple_users():
    group3_csv = "Eclipse,Doom,Deepakchopra,Czaraza,Chucktar,Gloom,djhedgehog,criddy,Dawnchorus,Xyzper,Bujsaim"
    result = create_raid_helper_cmd(event_id="123", user_csv=group3_csv)
    assert result.startswith("!adduser 123 ")
    expected_roles = ["Combat [Doom]", "Protection [Eclipse]", "Restoration1 [Deepakchopra]",
                      "Elemental [Czaraza]", "Destruction [Chucktar]", "Fire [Djhedgehog, Gloom]",
                      "Beastmastery [Xyzper]", "Restoration [Bujsaim]"]
    for role in expected_roles:
        assert role in result


def test_create_raid_helper_cmd_single_user():
    result = create_raid_helper_cmd(event_id="766085748331511870", user_csv="Doom")
    assert result == "!adduser 766085748331511870 Combat [Doom]"


def test_get_roles_for_users_single_user():
    assert get_roles_for_users("Doom") == ["Combat [Doom]"]


@pytest.mark.parametrize("user,role", [
    ["Doom", "Combat"], ["TommySalami", "Combat"], ["Muggsyrogue", "Combat"],
    ["Gluchy", "Fury"], ["Mahomes", "Fury"], ["Titan", "Fury"],
    ["Vonsky", "Protection"], ["Eclipse", "Protection"],
    ["Masque", "Guardian"],
    ["Bujsaim", "Restoration"],
    ["Drink", "Balance"],
    ["Itank", "Protection1"],
    ["HEEM", "Retribution"],
    ["Dawnchorus", "Holy1"], ["Yuli", "Holy1"],
    ["Xyzper", "Beastmastery"], ["Tendo", "Beastmastery"], ["Javajunkie", "Beastmastery"],
    ["Bariz", "Survival"],
    ["Criddy", "Shadow"], ["Melty", "Shadow"], ["Deathbite", "Shadow"],
    ["Astaniss", "Holy"], ["Zilf", "Holy"],
    ["Djhedgehog", "Fire"], ["Phaser", "Fire"], ["Principes/Ma", "Fire"], ["Gloom", "Fire"],
    ["Chucktar", "Destruction"], ["Boaz", "Destruction"],
    ["Pookin", "Affliction"],
    ["Mole", "Elemental"], ["Czaraza", "Elemental"],
    ["Remdesivir", "Restoration1"], ["Deepakchopra", "Restoration1"], ["Killersweets", "Restoration1"],
    ["Pralinka", "Restoration1"]
])
def test_get_role_for_user_single_user(user: str, role: str):
    assert get_role_for_user(user) == role
