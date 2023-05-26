<?php
/**
 * Mesa WPEX functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package WordPress
 * @subpackage Mesa WPEX
 * @since WPEX 1.0
 */

/**
 * Alters the default excerpt length.
 *
 * @since WPEX 1.0
 *
 * @param int $number The maximum number of words. Default 55.
 */
if ( ! function_exists( 'mesa_wpex_excerpt_length' ) ) :
	function mesa_wpex_excerpt_length( $number ) {
		$number = 25;
		return $number;
	}
	add_filter( 'excerpt_length', 'mesa_wpex_excerpt_length' );
endif;

/**
 * Alters the default excerpt_more string.
 *
 * @since WPEX 1.0
 *
 * @param string $more_string The string shown within the more link.
 */
if ( ! function_exists( 'mesa_wpex_excerpt_more' ) ) :
	function mesa_wpex_excerpt_more( $more_string ) {
		$more_string = '&hellip;';
		return $more_string;
	}
	add_filter( 'excerpt_more', 'mesa_wpex_excerpt_more' );
endif;