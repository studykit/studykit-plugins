# MoveFeature.inputEntities Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Gets and sets the entities to move. This is done by using an ObjectCollection containing the objects to move. For a parametric model, the collection can contain BRepBody or BRepFace objects but not a combination of both.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object.  ```` ``` # Get the value of the property. propertyValue = moveFeature_var.inputEntities  # Set the value of the property. moveFeature_var.inputEntities = propertyValue ``` ```` |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = moveFeature_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = moveFeature_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |