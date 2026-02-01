# CombineFeatureInput.isKeepToolBodies Property

Parent Object: [CombineFeatureInput](CombineFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatureInput.h>

## Description

Gets and sets a boolean value for whether or not the tool bodies are retrained after the combine results. The default value is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. |

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. ```` ``` #include <Fusion/Features/CombineFeatureInput.h>  // Get the value of the property. boolean propertyValue = combineFeatureInput_var->isKeepToolBodies();  // Set the value of the property, where value_var is a boolean. bool returnValue = combineFeatureInput_var->isKeepToolBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |