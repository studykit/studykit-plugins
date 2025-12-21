# RibDefinition.ExtentDistance Property

Parent Object: [RibDefinition](../RibDefinition/RibDefinition.md)

## Description

Read-only property that returns the parameter that corresponds to the distance value for rib feature defined with a finite extent. This property returns a parameter only if the ExtentType is kFiniteRibExtent, else this property returns Nothing. Also, in the case where this is a newly created RibDefinition object or it has been copied from an existing RibDefinition object, this property returns Nothing since there isn’t a parameter created yet.

## Syntax

RibDefinition.**ExtentDistance**() As Variant

## Property Value

This is a read only property whose value is a Variant.

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |