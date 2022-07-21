import http from 'k6/http';
import { FormData } from 'https://jslib.k6.io/formdata/0.0.2/index.js';
import { sleep } from 'k6';

export default function () {
  const url = 'https://base-de-scrim-manager-api.herokuapp.com/scrim-search';

  var payload = new FormData();
  payload.append('user_id', '1');
  payload.append('team_name', 'lala');
  payload.append('team_elo', '8');
  payload.append('order_elo', '1');
  payload.append('scrim_date', '1658358030');

  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + payload.boundary },
  };

  http.post(url, payload.body(), params);
  sleep(1);
}