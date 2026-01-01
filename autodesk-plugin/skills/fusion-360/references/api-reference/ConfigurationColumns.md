# ConfigurationColumns Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Returns a collection of the columns in the table. The Name column is not included in this list.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addClearanceTypeColumns](ConfigurationColumns_addClearanceTypeColumns.htm) | Creates the columns in the configuration table to control the clearance information associated with a clearance hole. Because configuring a clearance hole requires several pieces of related information, this method collects it all at once and creates all the corresponding feature aspect columns. |
| [addFeatureAspectColumn](ConfigurationColumns_addFeatureAspectColumn.htm) | Creates a new column to control an aspect of a feature that supports being configured. |
| [addInsertColumn](ConfigurationColumns_addInsertColumn.htm) | Add a new column to control which configuration is used for an inserted configuration. If an insert column already exists for the occurrence, the existing column is returned.   This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types. |
| [addInsertStandardDesignColumn](ConfigurationColumns_addInsertStandardDesignColumn.htm) | Add a new column to control which standard design is used for an inserted design. If an inserted column already exists for the occurrence, the existing column is returned.   This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types. |
| [addParameterColumn](ConfigurationColumns_addParameterColumn.htm) | Adds a new parameter column to the configuration table. If a parameter column already exists for the parameter, the existing column is returned.   This is only valid for TopConfigurationTable and ThemeConfigurationTable objects. It will fail for all other table types. |
| [addPropertyColumn](ConfigurationColumns_addPropertyColumn.htm) | Add a new column to control the property inside the component. The component is the owner of the property. This is only valid for TopConfigurationTable. It will fail for all other table types. |
| [addSuppressColumn](ConfigurationColumns_addSuppressColumn.htm) | Adds a new column to control the suppression of a feature. The term "feature" is used broadly and includes anything displayed in the timeline. If a suppression column already exists for the feature, the existing column is returned.   This is only valid for TopConfigurationTable and ThemeConfigurationTable objects. It will fail for all other table types. |
| [addThreadTypeColumns](ConfigurationColumns_addThreadTypeColumns.htm) | Creates the columns in the configuration table to control the type of thread associated with a thread feature or a tapped hole. Because configuring a thread requires several pieces of information, this method collects it all at once and creates all the corresponding feature aspect columns. |
| [addVisibilityColumn](ConfigurationColumns_addVisibilityColumn.htm) | Adds a new column to control the visibility of an entity. If a visibility column already exists for the entity, the existing column is returned.   This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types. |
| [classType](ConfigurationColumns_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ConfigurationColumns_item.htm) | A method that returns the specified column object using an index into the collection. |
| [itemById](ConfigurationColumns_itemById.htm) | A method that returns the specified column object using the ID of the column. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ConfigurationColumns_count.htm) | Returns the number of columns in the table. The name column is not included. |
| [isValid](ConfigurationColumns_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationColumns_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[ConfigurationCustomThemeTable.columns](ConfigurationCustomThemeTable_columns.htm), [ConfigurationTopTable.columns](ConfigurationTopTable_columns.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |