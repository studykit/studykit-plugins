# CustomGraphicsPointSet.indexList Property

Parent Object: [CustomGraphicsPointSet](CustomGraphicsPointSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsPointSet.h>

## Description

An list of indices that specify which coordinates from the coordinate list to draw points for. If this is an empty array, then all of the coordinates are used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. |

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. ```` ``` #include <Fusion/Graphics/CustomGraphicsPointSet.h>  // Get the value of the property. std::vector<integer> propertyValue = customGraphicsPointSet_var->indexList();  // Set the value of the property, where value_var is an integer. bool returnValue = customGraphicsPointSet_var->indexList(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |