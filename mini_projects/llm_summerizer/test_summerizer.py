from summerizer import summarize, chunk_text
from unittest.mock import patch, MagicMock
import requests

def test_chunk_text():
    assert chunk_text("abcdefghij", 4) == ['abcd', 'efgh', 'ij']
    assert chunk_text("abc", 10) == ['abc']
    assert chunk_text("", 4) == []

@patch("summerizer.requests.post")
def test_summarize(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"response": "fake summary"}
    

    assert summarize("any text") == "fake summary"
    mock_post.assert_called_once()


@patch("summerizer.requests.post")
@patch("summerizer.time.sleep")
def test_retry(mock_sleep, mock_post):
    good_reply = MagicMock()
    good_reply.status_code = 200
    good_reply.json.return_value = {"response": "fake summary"}

    mock_post.side_effect = [requests.exceptions.ConnectionError(), good_reply]

    assert summarize("any text") == "fake summary"
    assert mock_post.call_count == 2
    