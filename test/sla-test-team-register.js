import http from 'k6/http';
import { FormData } from 'https://jslib.k6.io/formdata/0.0.2/index.js';
import { sleep } from 'k6';

export default function () {
  const url = 'https://base-de-scrim-manager-api.herokuapp.com/team-register';

  var payload = new FormData();
  payload.append('user_id', '1');
  payload.append('team_name', 'lala');

  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + payload.boundary },
  };

  http.post(url, payload.body(), params);
  sleep(1);
}