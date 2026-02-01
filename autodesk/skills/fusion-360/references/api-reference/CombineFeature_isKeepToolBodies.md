# CombineFeature.isKeepToolBodies Property

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

Gets and sets a boolean value for whether or not the tool bodies are retrained after the combine results.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a CombineFeature object.  ```` ``` # Get the value of the property. propertyValue = combineFeature_var.isKeepToolBodies  # Set the value of the property. combineFeature_var.isKeepToolBodies = propertyValue ``` ```` |

"combineFeature\_var" is a variable referencing a CombineFeature object. ```` ``` #include <Fusion/Features/CombineFeature.h>  // Get the value of the property. boolean propertyValue = combineFeature_var->isKeepToolBodies();  // Set the value of the property, where value_var is a boolean. bool returnValue = combineFeature_var->isKeepToolBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |