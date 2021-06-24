from . import bp as blog
from app import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .forms import PostForm, DeletePostForm
from .models import Post


@blog.route('/createcontact', methods=['GET', 'POST'])
@login_required
def createcontact():
    title = 'CREATE CONTACT'
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post_firstname = form.firstname.data
        post_lastname = form.lastname.data
        post_email =  form.email.data
        post_address = form.address.data
        post_phonenumber = form.phonenumber.data
        user_id = current_user.id

        new_post = Post(post_firstname, post_lastname, post_email, post_address, post_phonenumber, user_id)

        db.session.add(new_post)
        db.session.commit()

        flash(f"You have created a post: {post_firstname}", 'info')

        return redirect(url_for('main.index'))

    return render_template('createcontact.html', title=title, form=form)


@blog.route('/contacts')
@login_required
def contacts():
    title = 'MY CONTACTS'
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('contacts.html', title=title, posts=posts)


@blog.route('/contacts/<int:post_id>')
def contact_detail(post_id):
    post = Post.query.get_or_404(post_id)
    context = {
        'post': post,
        'title': post.firstname,
        'form': DeletePostForm()
    }
    return render_template('contact_detail.html', **context)


@blog.route('/contacts/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def contacts_update(post_id):
    post = Post.query.get_or_404(post_id)
    title = f'UPDATE {post.title}'
    if post.author.id != current_user.id:
        flash("You cannot update another user's contacts.", "warning")
        return redirect(url_for('blog.mycontacts'))
    update_form = PostForm()
    if request.method == 'POST' and update_form.validate_on_submit():
        post_firstname = update_form.firstname.data
        post_lastname = update_form.lastname.data
        post_email = update_form.email.data
        post_address = update_form.address.data
        post_phonenumber = update_form.phonenumber.data
        

        post.firstname = post_firstname
        post.lastname = post_lastname
        post.email = post_email
        post.address = post_address
        post.phonenumber = post_phonenumber

        db.session.commit()

        return redirect(url_for('blog.contact_detail', post_id=post.id))

    return render_template('contact_update.html', title=title, post=post, form=update_form)


@blog.route('/contacts/delete/<int:post_id>', methods=['POST'])
@login_required
def contact_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != current_user.id:
        flash("You cannot delete another user's contact.", "warning")
        return redirect(url_for('blog.mycontacts'))
    form = DeletePostForm()
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        flash(f'{post.title} has been deleted', 'info')
        return redirect(url_for('blog.mycontacts'))
    return redirect(url_for('main.index'))