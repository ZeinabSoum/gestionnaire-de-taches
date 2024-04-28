import click

tasks = []  # Liste pour stocker les tâches

@click.group()
def cli():
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Ajoute une tâche à la liste."""
    tasks.append({'task': task, 'completed': False})
    click.echo(f'Tâche ajoutée : {task}')

@cli.command()
@click.option('--completed', is_flag=True, help='Affiche uniquement les tâches terminées.')
@click.option('--incomplete', is_flag=True, help='Affiche uniquement les tâches non terminées.')
def list(completed, incomplete):
    """Affiche les tâches de la liste."""
    if not tasks:
        click.echo("La liste des tâches est vide.")
        return

    if completed and incomplete:
        click.echo("Impossible de spécifier à la fois --completed et --incomplete.")
        return

    if completed:
        filtered_tasks = [task for task in tasks if task['completed']]
    elif incomplete:
        filtered_tasks = [task for task in tasks if not task['completed']]
    else:
        filtered_tasks = tasks

    click.echo("Liste des tâches :")
    for index, task in enumerate(filtered_tasks, start=1):
        status = 'X' if task['completed'] else ' '
        click.echo(f"{index}. [{status}] {task['task']}")

@cli.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Supprime une tâche de la liste."""
    if 1 <= task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        click.echo(f'Tâche supprimée : {task["task"]}')
    else:
        click.echo("Numéro de tâche invalide.")

@cli.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Marque une tâche comme terminée."""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        click.echo(f'Tâche marquée comme terminée : {tasks[task_number - 1]["task"]}')
    else:
        click.echo("Numéro de tâche invalide.")

if __name__ == '__main__':
    cli()
