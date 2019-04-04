## [1.1.1] 3/4/2019
### Added
 - backwards compatibility testing with `tox`
 - qa support

### Fixed
 - Quote failing to set `token`

## [1.1.0] 2/4/2019
### Updated
 - Compatibility with Python2.7

### Fixed
 - Lazy load list slice
 - Patch tests that were failing

### Added
 - Auth class
 - Scope property for Client and Affiliate
 - Parent Scope property for Affiliate
 - User class that supports retrieve, list, and update.
 - Update and Partial Update examples on README

### Changed
 - `.update()` and `.patch()` will use the Object's `id` by default. Changed from having to pass `id` as an argument.

## [1.0.1]
 - Core URL

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