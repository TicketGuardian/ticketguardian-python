## [Unreleased]
### Updated
 - Compatibility with Python2.7

### Fixed
 - Lazy load list slice
 - Patch tests that were failing
 - Core URL

### Added
 - Affiliate method to get all parent Affiliates


## [1.0.0] 1/21/2019
### Added
 - Lazy load list and iterator (Not 100% complete but okay for internal use)
 - Lazy load iterator which only stores the current page of objects
 - credentials file for a users set of keys
 - Example showing how to use the sdk for quoting items, creating an order, and charging the order.
 - A requirements directory
 - PATCH capabilities for Affiliate, Client, and Order

### Updated
 - README
 - Renamed tg_sdk to ticketguardian

### Fixed
 - Bug in __repr__ which threw an exception for objects without the attribute id

### Removed
 - Requirements.txt