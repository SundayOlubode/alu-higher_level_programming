-- Root user

CREATE USER user_0d_1 IF NOT EXISTS IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
