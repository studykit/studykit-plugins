# LoftCenterLineOrRail.entity Property

Parent Object: [LoftCenterLineOrRail](LoftCenterLineOrRail.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftCenterLineOrRail.h>

## Description

Gets and sets the entity that defines the centerline or rail. This can be a single sketch entity, a single BRepEdge, a Path, or a Profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftCenterLineOrRail\_var" is a variable referencing a LoftCenterLineOrRail object.  ```` ``` # Get the value of the property. propertyValue = loftCenterLineOrRail_var.entity  # Set the value of the property. loftCenterLineOrRail_var.entity = propertyValue ``` ```` |

"loftCenterLineOrRail\_var" is a variable referencing a LoftCenterLineOrRail object. ```` ``` #include <Fusion/Features/LoftCenterLineOrRail.h>  // Get the value of the property. Ptr<Base> propertyValue = loftCenterLineOrRail_var->entity();  // Set the value of the property, where value_var is a Base. bool returnValue = loftCenterLineOrRail_var->entity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |