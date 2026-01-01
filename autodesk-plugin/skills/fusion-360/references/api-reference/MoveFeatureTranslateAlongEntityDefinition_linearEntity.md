# MoveFeatureTranslateAlongEntityDefinition.linearEntity Property

Parent Object: [MoveFeatureTranslateAlongEntityDefinition](MoveFeatureTranslateAlongEntityDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureTranslateAlongEntityDefinition.h>

## Description

Gets and sets the linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureTranslateAlongEntityDefinition\_var" is a variable referencing a MoveFeatureTranslateAlongEntityDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureTranslateAlongEntityDefinition_var.linearEntity  # Set the value of the property. moveFeatureTranslateAlongEntityDefinition_var.linearEntity = propertyValue ``` ```` |

"moveFeatureTranslateAlongEntityDefinition\_var" is a variable referencing a MoveFeatureTranslateAlongEntityDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureTranslateAlongEntityDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = moveFeatureTranslateAlongEntityDefinition_var->linearEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = moveFeatureTranslateAlongEntityDefinition_var->linearEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |