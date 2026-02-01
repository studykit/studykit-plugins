# ModelHoleThreadNoteDefinition.Parent Property

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object.

## Syntax

ModelHoleThreadNoteDefinition.**Parent**() As [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md)

## Property Value

This is a read only property whose value is a [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md).

## Version

Introduced in version 2018
