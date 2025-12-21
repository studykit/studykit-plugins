# RibDefinition.ExtentType Property

Parent Object: [RibDefinition](../RibDefinition/RibDefinition.md)

## Description

Read-only property that returns the extent type of the rib feature. The possible return values are kFiniteRibExtent and kToNextRibExtent. When the RibDefinition object is initially created, this defaults to kToNextRibExtent. If this property returns kFiniteRibExtent, the ExtentDistance property returns the correspond parameter. Use the SetFiniteExtent and Set ToNextExtent methods to edit the extent type.

## Syntax

RibDefinition.**ExtentType**() As [RibFeatureExtentEnum](../RibFeatureExtentEnum.md)

## Property Value

This is a read only property whose value is a [RibFeatureExtentEnum](../RibFeatureExtentEnum.md).

## Version

Introduced in version 2012
