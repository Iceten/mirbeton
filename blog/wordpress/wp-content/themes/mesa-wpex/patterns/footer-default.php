<?php
/**
 * Title: Default Footer
 * Slug: mesa-wpex/footer-default
 * Categories: footer
 * Block Types: core/template-part/footer
 */
?>
<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group">
	<!-- wp:group {"align":"wide","style":{"spacing":{"margin":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
	<div class="wp-block-group alignwide" style="margin-top:var(--wp--preset--spacing--large);margin-bottom:var(--wp--preset--spacing--large)">
		<!-- wp:paragraph {"align":"center"} -->
		<p class="has-text-align-center"><?php
		echo sprintf(
			/* translators: %1$s: Copyright html symbol,  %2$s: Year, %3$s: Vendor link */
			esc_html_x( 'Copyright %1$s %2$s', '1: Copyright html symbol 2: Year', 'mesa-wpex' ),
			'&copy;',
			esc_attr( date_i18n( __( 'Y', 'mesa-wpex' ) ) )
			)
		. ' &vert; ' .
		sprintf(
			/* Translators: WPExplorer link. */
			esc_html__( 'Theme by %s', 'mesa-wpex' ),
			'<a href="https://www.wpexplorer.com/" target="_blank">WPExplorer</a>'
		);
		?></p>
		<!-- /wp:paragraph -->
	</div>
	<!-- /wp:group -->
</div>
<!-- /wp:group -->
