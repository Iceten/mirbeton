<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'mirbetonblogdb' );

/** Database username */
define( 'DB_USER', 'idrissdbuser' );

/** Database password */
define( 'DB_PASSWORD', 'Godsuccess-555' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '/F@O[Ci{Z-Vq%KI&TJ =Kyg|LobQ?=?**xM!.Yfy0aWif$fI{e%~F=]H;Wpplh^=' );
define( 'SECURE_AUTH_KEY',  '#mcz{16}*uLY{pZ*U^Hlt+AZ}ss$4%)qF[LidHoDe>6()vgMx/+Cz/%l<uu$fmlk' );
define( 'LOGGED_IN_KEY',    'TaD*xQY7+M4JV^xpU}CHL$`L/RQh,I2}zw{G{7`Xy|&oG)=;^E>*aTIt+B6AC=<h' );
define( 'NONCE_KEY',        ']j2v _P{om~Hqy^}q )Y#qH9`A[:U8sleV>!WM-$5kZ{5$,p&bvB]xVk^h$wi<H_' );
define( 'AUTH_SALT',        'nH>%Es&J)O~tyF=B%ZtbyJ2V={os.Q-11f8G2=sKQ+?y7^FI0e2Hxd~.._gx Zbg' );
define( 'SECURE_AUTH_SALT', ',Bgr2dmt3sLu<<C9I;lb}x!aXKH_$>F.W/Vz({0Ze4w0e-+qp[_;s%epmJydJ@vX' );
define( 'LOGGED_IN_SALT',   'N}1s>EUZJP1:g G5>{Kg_gc#`p1KuN%ecTo9k@F)J=]-y):~?09z5$&&RKT@amJh' );
define( 'NONCE_SALT',       '{dT:3Ng}HMU7oU;Ym_c*g5+(1swztz+:=3xmalE%eXj_:jQf`jBVFEaYB#2:h-a(' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
