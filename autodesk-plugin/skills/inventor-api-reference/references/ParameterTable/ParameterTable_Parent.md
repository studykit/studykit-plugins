# ParameterTable.Parent Property

Parent Object: [ParameterTable](../ParameterTable/ParameterTable.md)

## Description

Property that returns the parent object of this ParameterTable. This property will return different types of objects depending on the document type the ParameterTable is contained in. If the ParameterTable is in a part document then the parent is a PartComponentDefinition object. If the ParameterTable is in an assembly document then the parent is an AssemblyComponentDefinition. If the document is a drawing document then the parent is a DraftDocument.

## Syntax

ParameterTable.**Parent**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 4
