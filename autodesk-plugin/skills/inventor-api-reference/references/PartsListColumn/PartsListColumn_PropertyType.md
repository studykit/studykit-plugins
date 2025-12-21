# PartsListColumn.PropertyType Property

Parent Object: [PartsListColumn](../PartsListColumn/PartsListColumn.md)

## Description

Property that returns the property type associated with this column. If this property returns kFilePropertyType, the GetFilePropertyId method returns the identity of the file property. If this property returns kCustomPropertyType, use the CustomPropertyName property to get the name of the custom property.

## Syntax

PartsListColumn.**PropertyType**() As [PropertyTypeEnum](../PropertyTypeEnum.md)

## Property Value

This is a read only property whose value is a [PropertyTypeEnum](../PropertyTypeEnum.md).

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |