# LoftDefinition.Centerline Property

Parent Object: [LoftDefinition](../LoftDefinition/LoftDefinition.md)

## Description

Property that specifies the centerline for the loft. Valid objects includes Profile, Profile3D, EdgeLoop and EdgeCollection. When this LoftDefinition is associative with an existing LoftFeature or if it is copied from an LoftDefinition that is associative with a LoftFeature, then set this property you should follow below rules, otherwise an error would occur:

* If the LoftDefinition.LoftType returns kRegularLoft you can set this property directly.
* If the LoftDefinition.LoftType returns kLoftWithRails you need to clear the LoftDefinition.LoftRails before setting this property.
* If the LoftDefinition.LoftType returns kLoftWithAreaGraphSections you need to clear the LoftDefinition.LoftSectionDimensions if any before setting this property,

## Syntax

LoftDefinition.**Centerline**() As Object

## Property Value

This is a read/write property whose value is an Object.

## Version

Introduced in version 2008
