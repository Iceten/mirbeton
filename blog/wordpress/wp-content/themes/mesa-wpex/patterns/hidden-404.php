<?php
/**
 * Title: Hidden 404
 * Slug: mesa-wpex/hidden-404
 * Inserter: no
 */
?>
<!-- wp:spacer {"height":"var(--wp--preset--spacing--x-large)"} -->
<div style="height:var(--wp--preset--spacing--x-large)" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->


<!-- wp:heading {"level":1,"align":"wide","textAlign":"center"} -->
<h1 class="alignwide has-text-align-center"><?php echo esc_html__( 'Page Not Found', 'mesa-wpex' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:group {"align":"wide","layout":{"type":"default"},"style":{"spacing":{"margin":{"top":"var:preset|spacing|small"}}}} -->
<div class="wp-block-group alignwide" style="margin-top:var(--wp--preset--spacing--small);">
	<!-- wp:paragraph {"align":"center"} -->
	<p class="has-text-align-center"><?php echo sprintf( esc_html_x( 'The page you were looking for was moved, removed, renamed or may have never existed. %s You can use the field below to try and find what you were looking for.', 'Message to convey that a webpage could not be found', 'mesa-wpex' ), '<br>' ); ?></p>
	<!-- /wp:paragraph -->

	<!-- wp:search {"label":"<?php echo esc_html_x( 'Search', 'label', 'mesa-wpex' ); ?>","placeholder":"<?php echo esc_attr_x( 'Search...', 'placeholder for search field', 'mesa-wpex' ); ?>","showLabel":false,"width":500,"widthUnit":"px","buttonText":"<?php esc_attr_e( 'Search', 'mesa-wpex' ); ?>","buttonUseIcon":true,"align":"center"} /-->
</div>
<!-- /wp:group -->

<!-- wp:spacer {"height":"var(--wp--preset--spacing--x-large)"} -->
<div style="height:var(--wp--preset--spacing--x-large)" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
