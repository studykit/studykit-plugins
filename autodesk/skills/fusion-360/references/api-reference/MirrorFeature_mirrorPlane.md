# MirrorFeature.mirrorPlane Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Gets and sets the mirror plane. This can be either a planar face or construction plane. This works only for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object.  ```` ``` # Get the value of the property. propertyValue = mirrorFeature_var.mirrorPlane  # Set the value of the property. mirrorFeature_var.mirrorPlane = propertyValue ``` ```` |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = mirrorFeature_var->mirrorPlane();  // Set the value of the property, where value_var is a Base. bool returnValue = mirrorFeature_var->mirrorPlane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |