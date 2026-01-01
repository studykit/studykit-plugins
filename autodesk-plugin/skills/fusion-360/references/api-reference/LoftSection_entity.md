# LoftSection.entity Property

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Get and sets the entity that defines the section of the loft. This can be a BRepFace, Profile, Path, SketchPoint, ConstructionPoint, or an ObjectCollection of contiguous profiles.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a LoftSection object.  ```` ``` # Get the value of the property. propertyValue = loftSection_var.entity  # Set the value of the property. loftSection_var.entity = propertyValue ``` ```` |

"loftSection\_var" is a variable referencing a LoftSection object. ```` ``` #include <Fusion/Features/LoftSection.h>  // Get the value of the property. Ptr<Base> propertyValue = loftSection_var->entity();  // Set the value of the property, where value_var is a Base. bool returnValue = loftSection_var->entity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |