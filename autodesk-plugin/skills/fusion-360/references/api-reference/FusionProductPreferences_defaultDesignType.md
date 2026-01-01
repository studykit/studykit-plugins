# FusionProductPreferences.defaultDesignType Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets the default modeling type setting

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. DefaultDesignTypeOptions propertyValue = fusionProductPreferences_var->defaultDesignType();  // Set the value of the property, where value_var is a DefaultDesignTypeOptions. bool returnValue = fusionProductPreferences_var->defaultDesignType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DefaultDesignTypeOptions](DefaultDesignTypeOptions.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |