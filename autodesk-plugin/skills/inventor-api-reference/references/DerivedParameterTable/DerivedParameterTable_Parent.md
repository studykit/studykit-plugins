# DerivedParameterTable.Parent Property

Parent Object: [DerivedParameterTable](../DerivedParameterTable/DerivedParameterTable.md)

## Description

Property that returns the parent object of this DerivedParameterTable. This property will return different types of objects depending on the document type the DerivedParameterTable is contained in. If the DerivedParameterTable is in a part document then the parent is a PartComponentDefinition object. If the DerivedParameterTable is in an assembly document then the parent is an AssemblyComponentDefinition.

## Syntax

DerivedParameterTable.**Parent**() As Object

## Property Value

This is a read only property whose value is an Object.

## Version

Introduced in version 11
