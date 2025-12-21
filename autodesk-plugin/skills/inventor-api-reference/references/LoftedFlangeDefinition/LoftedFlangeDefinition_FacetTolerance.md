# LoftedFlangeDefinition.FacetTolerance Property

Parent Object: [LoftedFlangeDefinition](../LoftedFlangeDefinition/LoftedFlangeDefinition.md)

## Description

Property that returns the parameter controlling the tolerance used to calculate the lofted flange. This will return Nothing in the case where the OutputType property returns kDieFormedLoftedFlange and where the LoftedFlangeDefinition object is not associated with an existing lofted flange.

## Syntax

LoftedFlangeDefinition.**FacetTolerance**() As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Version

Introduced in version 2011
