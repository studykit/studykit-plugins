# ConfigurationFeatureAspectColumn.feature Property

Parent Object: [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>

## Description

Returns the feature being controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectColumn\_var" is a variable referencing a ConfigurationFeatureAspectColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationFeatureAspectColumn_var.feature ``` ```` |

"configurationFeatureAspectColumn\_var" is a variable referencing a ConfigurationFeatureAspectColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationFeatureAspectColumn_var->feature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |