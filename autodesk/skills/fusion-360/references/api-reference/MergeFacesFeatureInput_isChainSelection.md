# MergeFacesFeatureInput.isChainSelection Property

Parent Object: [MergeFacesFeatureInput](MergeFacesFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatureInput.h>

## Description

Get and sets whether or not faces that are tangentially connected and from the same body (solid or surface) will be included in the faces to merge

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. |

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. ```` ``` #include <Fusion/Features/MergeFacesFeatureInput.h>  // Get the value of the property. boolean propertyValue = mergeFacesFeatureInput_var->isChainSelection();  // Set the value of the property, where value_var is a boolean. bool returnValue = mergeFacesFeatureInput_var->isChainSelection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |