import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    first = encrypt_message("AABBCC", -1)
    assert first == "CCBBAA"

    second = encrypt_message("AABBCC", 3)
    assert second == "BAA_CCB"

    third = encrypt_message("ABBCCA", 4)
    assert third == "AC_CBBA"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("AABBCC", "-1")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 3)
