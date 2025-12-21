# RibDefinition.Copy Method

Parent Object: [RibDefinition](../RibDefinition/RibDefinition.md)

## Description

Method that creates a copy of this RibDefinition object. The new RibDefinition object is independent of any feature. It can be edited and used as input to edit an existing feature or to create a new Rib feature.

One typical use of this method is when you need to make several changes to an existing Rib feature. If you edit the RibDefinition object associated with the Rib feature, the feature will recompute after each edit. It’s more efficient to make a copy, edit the copy, and then assign the copy to the feature. This will result in a single recompute.

The RibFeatures.CreateDefinition method can also be used to create an independent RibDefinition object. The difference is that one created with the Copy method will have the same initial values as the object is was copied from. One that’s created with the CreateDefinition method will be initialized to predefined default values.

## Syntax

RibDefinition.**Copy**() As [RibDefinition](../RibDefinition/RibDefinition.md)

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |