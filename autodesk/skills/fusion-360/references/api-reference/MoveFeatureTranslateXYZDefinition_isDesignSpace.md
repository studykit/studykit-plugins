# MoveFeatureTranslateXYZDefinition.isDesignSpace Property

Parent Object: [MoveFeatureTranslateXYZDefinition](MoveFeatureTranslateXYZDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureTranslateXYZDefinition.h>

## Description

Gets and sets if the translation is defined with respect to the design or component space. Design space is the same as the root component space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureTranslateXYZDefinition\_var" is a variable referencing a MoveFeatureTranslateXYZDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureTranslateXYZDefinition_var.isDesignSpace  # Set the value of the property. moveFeatureTranslateXYZDefinition_var.isDesignSpace = propertyValue ``` ```` |

"moveFeatureTranslateXYZDefinition\_var" is a variable referencing a MoveFeatureTranslateXYZDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureTranslateXYZDefinition.h>  // Get the value of the property. boolean propertyValue = moveFeatureTranslateXYZDefinition_var->isDesignSpace();  // Set the value of the property, where value_var is a boolean. bool returnValue = moveFeatureTranslateXYZDefinition_var->isDesignSpace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |