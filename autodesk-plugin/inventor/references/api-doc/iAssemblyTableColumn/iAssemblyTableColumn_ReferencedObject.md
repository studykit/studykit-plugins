# iAssemblyTableColumn.ReferencedObject Property

Parent Object: [iAssemblyTableColumn](../iAssemblyTableColumn/iAssemblyTableColumn.md)

## Description

Property that returns the object referenced by the column. For instance, if the column references a fillet feature suppression, the corresponding FilletFeature object is returned. Similarly, if a file property is referenced, the corresponding Property object is returned.  The property returns Nothing if there is no corresponding object (e.g. when the ReferencedDataType returns kMemberNameColumn).

## Syntax

iAssemblyTableColumn.**ReferencedObject**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |