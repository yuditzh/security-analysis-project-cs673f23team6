import BaseLayout from './layout/BaseLayout';
import Home from './pages/Home';
import Marketplace from './pages/Marketplace';
import Product from './pages/Product';
import User from './pages/User';
import Chat from './pages/Chat';
import Password from './pages/Password'

const routes = [
  {
    path: '',
    element: <BaseLayout />,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: '/marketplace',
        element: <Marketplace />,
      },
      {
        path: '/product/:id',
        element: <Product />,
      },
      {
        path: '/user/:id',
        element: <User />,
      },
      {
        path: '/chat/:id',
        element: <Chat />,
      },
      {
        path: '/forgot-password',
        element: <Password />
      },
    ],
  },
];

export default routes;
