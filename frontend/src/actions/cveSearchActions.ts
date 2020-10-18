import axios from 'axios';

export const actions: Record<string, string> = {
  FETCH_DATA_REQUEST: 'FETCH_DATA_REQUEST',
  FETCH_DATA_SUCCESS: 'FETCH_DATA_SUCCESS',
  FETCH_DATA_FAILURE: 'FETCH_DATA_FAILURE',
};

export const fetchData = (searchCve: string, tabIndex: number) => (
  dispatch: Function,
) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST, payload: { tabIndex } });

  return axios
    .get(`http://localhost:8000/search/cve/${searchCve}`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_DATA_SUCCESS,
        payload: {
          tabIndex,
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_DATA_FAILURE,
        payload: {
          tabIndex,
          error: err.message,
        },
      });
    });
};
