# MoveFeatureInput.inputEntities Property

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

An ObjectCollection containing the objects to move. The collection can contain BRepBody or BRepFace objects but not a mixture of the two types.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object. |

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object. ```` ``` #include <Fusion/Features/MoveFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = moveFeatureInput_var->inputEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = moveFeatureInput_var->inputEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |