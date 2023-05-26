<?php
/**
 * Title: Hidden No Results Content
 * Slug: mesa-wpex/hidden-no-results-content
 * Inserter: no
 */
?>

<!-- wp:group {"align":"wide","layout":{"type":"default"},"style":{"spacing":{"margin":{"top":"var:preset|spacing|small"}}}} -->
<div class="wp-block-group alignwide" style="margin-top:var(--wp--preset--spacing--small);">
    <!-- wp:paragraph {"align":"center"} -->
    <p class="has-text-align-center"><?php echo esc_html_x( 'Sorry, but nothing matched your search terms. Please try again with some different keywords.', 'Message explaining that there are no results returned from a search', 'mesa-wpex' ); ?></p>
    <!-- /wp:paragraph -->

    <!-- wp:search {"label":"<?php echo esc_html_x( 'Search', 'label', 'mesa-wpex' ); ?>","placeholder":"<?php echo esc_attr_x( 'Search...', 'placeholder for search field', 'mesa-wpex' ); ?>","showLabel":false,"width":500,"widthUnit":"px","buttonText":"<?php esc_attr_e( 'Search', 'mesa-wpex' ); ?>","buttonUseIcon":true,"align":"center"} /-->
</div>
<!-- /wp:group -->
