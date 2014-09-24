Reviews

In our shopping experience, user feedback is an important tool both for users and for suppliers. I'd like you to write a simple supplier reviews application.

Reviews will be made for energy suppliers. These suppliers have a name and a slug. A review consists of a rating between 1 and 5 inclusive, the name of the author, a time submitted, and the actual review.

The application consists of three pages:

Uri: /reviews

Title: Suppliers

This page should list the suppliers in the system and should include a link to each of the supplier reviews pages.

Url: /reviews/[supplier.slug]

Title: [supplier.name]

This page should list the published reviews for this supplier, most recent first. It should also include a link to the page for writing a review about this supplier.

Url: /reviews/[supplier-slug]/write

Title: Review [supplier.name]

This page should provide a form to submit new reviews.

In addition to the user facing pages, there should be a simple Django admin for verifying the reviews and changing the state from draft to published. Reviews should not appear on the supplier page unless they are published.