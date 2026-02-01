# ArrangeFeatureInput.definition Property

Parent Object: [ArrangeFeatureInput](ArrangeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatureInput.h>

## Description

Returns a definition input object that provides access to the information to define an arrange feature. This will return different types of definition inputs depending on the solver type specified when creating the input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object. |

"arrangeFeatureInput\_var" is a variable referencing an ArrangeFeatureInput object. ```` ``` #include <Fusion/Arrange/ArrangeFeatureInput.h>  // Get the value of the property. Ptr<ArrangeDefinitionInput> propertyValue = arrangeFeatureInput_var->definition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeDefinitionInput](ArrangeDefinitionInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |