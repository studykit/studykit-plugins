# AssemblyDocument.IsOpenExpress Property

Parent Object: [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md)

## Description

Read-write property that gets and sets a Boolean flag indicating whether this assembly is currently open in Express mode. When set this property it can only be set from True to False to load the document into full mode. To switch the document from full mode to express mode users should close it and re-open it in express mode using OpenWithOptions method.

## Syntax

AssemblyDocument.**IsOpenExpress**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Version

Introduced in version 2014
