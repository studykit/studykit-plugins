# MirrorFeature.inputEntities Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Gets and sets the entities that are mirrored. It can contain faces, features, bodies, or components. The input must all be of a single type. For example, you can't provide a body and a component but the collection must be either all bodies or all components.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object.  ```` ``` # Get the value of the property. propertyValue = mirrorFeature_var.inputEntities  # Set the value of the property. mirrorFeature_var.inputEntities = propertyValue ``` ```` |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = mirrorFeature_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = mirrorFeature_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |