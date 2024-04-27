import { useEffect, useState } from 'react';
import ProductCard from '../Components/ProductCard';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function Marketplace() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [data, setData] = useState({
    email: '',
  });
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!data.email) {
      setError('Please fill in all fields');
      return;
    }
    setLoading(true);
    const res = await axios.request('/api/users/password-reset', data);
    const resData = res.data;
    setLoading(false);
    navigate("/")
  };
  return (
    <div className="max-w-md mx-auto ">
      <div className="w-full ">
        <div className="p-2">
          <div className="flex flex-col items-center justify-center w-full gap-y-2">
            <h1 className="flex items-center gap-2 pb-2 text-3xl font-semibold text-gray-800 ">
              🎓
              <span>College Street</span>
            </h1>
          </div>
          <h2 className="mt-4 text-xl font-semibold text-left text-gray-800 ">
            Reset Password Form
          </h2>
          <p className="w-full mb-8 text-sm text-gray-500 dark:text-gray-400">
            Please enter the email you used to register
          </p>
          <form className="space-y-8">
            <div className="space-y-2">
              <input
                type="email"
                name="email"
                id="email"
                value={data.email}
                onChange={(e) => setData({ ...data, email: e.target.value })}
                placeholder="Email"
                autoComplete="username"
                className="focus:outline-none block w-full rounded-md border border-gray-200 dark:border-gray-600 bg-transparent px-4 py-3 text-gray-600 transition duration-300 invalid:ring-2 invalid:ring-red-400 focus:ring-2 focus:ring-[#9155FD]"
              />
            </div>

            <button
              type="submit"
              disabled={loading || !data.email}
              onClick={(e) => handleSubmit(e)}
              className="bg-[#9155FD] w-full p-2 rounded-xl hover:shadow-lg hover:bg-[#7e3af2] transition duration-300 "
            >
              {loading ? (
                <span className="relative flex items-center justify-center text-base font-semibold text-white ">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="currentColor"
                    className="w-6 h-6 animate-spin"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
                    />
                  </svg>
                </span>
              ) : (
                <span className="relative text-base font-semibold text-white ">
                  Send Email
                </span>
              )}
            </button>
            <div className="w-full pt-2 border-t border-black ">
              <button
                className="justify-end float-right pb-4 -mr-2"
                type="reset"
                onClick={() => {
                  handleSubmit()
                }}
              >
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}