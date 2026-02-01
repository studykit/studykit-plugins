# DSLoadDefinition.Magnitude Property

Parent Object: [DSLoadDefinition](../DSLoadDefinition/DSLoadDefinition.md)

## Description

Gets the DSValue object that defines the magnitude of the load. The value of the magnitude can be accessed through the returned DSValue object.

This property returns Nothing in the case where the IsDefinedByVectorComponents is True. To change the definition of the load to be defined by a magnitude and direction use the SetByMagnitudeAndDirection method.

Setting the magnitude using the SetValueUsingArray method of the DSValue object is currently limited to motion, magnitude, and x,y,z coordinates.

## Syntax

DSLoadDefinition.**Magnitude**() As [DSValue](../DSValue/DSValue.md)

## Property Value

This is a read only property whose value is a [DSValue](../DSValue/DSValue.md).

## Version

Introduced in version 2013
